const gplay = require('google-play-scraper').default;
const fs = require('fs');
const path = require('path');

const appIds = [
    'com.shankarbros.telugutoolkit',
    'com.shankarbros.hanumanchalisa',
    'com.shankarbros.ftpserver',
    'com.shankarbros.telugu2026calendarandrasiphalalu',
    'com.shankarbros.vastucompass',
    'com.shankarbros.teleprompter',
    'com.shankarbros.bubblelevel'
];

console.log(`Fetching details for ${appIds.length} apps...`);

const detailedApps = [];

const promises = appIds.map(id => 
    gplay.app({appId: id}).then(details => {
        detailedApps.push(details);
        console.log(`Scraped: ${details.title} | ⭐ ${details.score?.toFixed(1)} | 📥 ${details.installs}`);
    }).catch(err => {
        console.error(`Failed to scrape ${id}:`, err.message);
    })
);

Promise.all(promises).then(() => {
    // Write full app data
    const outputPath = path.join(__dirname, "apps_data.json");
    fs.writeFileSync(outputPath, JSON.stringify(detailedApps, null, 2));
    console.log("Successfully written to", outputPath);

    // Compute aggregated stats
    // Use score if available, else compute from histogram
    function getRating(app) {
        if (app.score && app.score > 0) return app.score;
        const h = app.histogram;
        if (!h) return null;
        const total = h[1] + h[2] + h[3] + h[4] + h[5];
        if (total === 0) return null;
        return (h[1]*1 + h[2]*2 + h[3]*3 + h[4]*4 + h[5]*5) / total;
    }

    const appsWithScore = detailedApps.map(getRating).filter(s => s !== null);
    const avgRating = appsWithScore.length > 0
        ? (appsWithScore.reduce((a, b) => a + b, 0) / appsWithScore.length).toFixed(1)
        : '4.8'; // fallback

    // Sum up minInstalls (numeric lower bound from Play Store)
    const totalInstalls = detailedApps.reduce((sum, a) => sum + (a.minInstalls || 0), 0);

    // Format installs nicely: e.g. 350000 -> "350k+"
    function formatInstalls(n) {
        if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(1)}M+`;
        if (n >= 1_000) return `${Math.floor(n / 1_000)}k+`;
        return `${n}+`;
    }

    const stats = {
        averageRating: parseFloat(avgRating),
        totalInstalls: totalInstalls,
        totalInstallsFormatted: formatInstalls(totalInstalls),
        appCount: detailedApps.length,
        lastUpdated: new Date().toISOString()
    };

    const statsPath = path.join(__dirname, '..', 'stats.json');
    fs.writeFileSync(statsPath, JSON.stringify(stats, null, 2));
    console.log(`\n📊 Stats written to ${statsPath}`);
    console.log(`   ⭐ Average Rating: ${stats.averageRating}`);
    console.log(`   📥 Total Installs: ${stats.totalInstallsFormatted} (${stats.totalInstalls.toLocaleString()})`);
});
