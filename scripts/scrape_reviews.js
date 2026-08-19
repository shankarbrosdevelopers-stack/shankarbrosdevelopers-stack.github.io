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

console.log(`Fetching reviews for ${appIds.length} apps...`);

const allReviews = [];

const promises = appIds.map(id => 
    gplay.reviews({
        appId: id,
        sort: gplay.sort.HELPFULNESS,
        num: 20 // Fetch top 20 reviews
    }).then(result => {
        const reviews = result.data || result; // Depending on google-play-scraper version
        if (reviews && Array.isArray(reviews)) {
            // Filter 5-star reviews and select up to 5 best ones
            const fiveStarReviews = reviews.filter(r => r.score === 5 && r.text && r.text.length > 20);
            
            fiveStarReviews.slice(0, 5).forEach(r => {
                allReviews.push({
                    appId: id,
                    userName: r.userName,
                    userImage: r.userImage,
                    score: r.score,
                    text: r.text,
                    date: r.date
                });
            });
            console.log(`Scraped ${fiveStarReviews.length} 5-star reviews for ${id}`);
        }
    }).catch(err => {
        console.error(`Failed to scrape reviews for ${id}:`, err.message);
    })
);

Promise.all(promises).then(() => {
    // Shuffle the reviews so they appear mixed
    for (let i = allReviews.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [allReviews[i], allReviews[j]] = [allReviews[j], allReviews[i]];
    }

    const outputPath = path.join(__dirname, "..", "reviews.json");
    fs.writeFileSync(outputPath, JSON.stringify(allReviews, null, 2));
    console.log(`Successfully written ${allReviews.length} reviews to ${outputPath}`);
});
