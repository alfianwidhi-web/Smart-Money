const fs = require('fs');
const html = fs.readFileSync('c:/Users/ALFIAN WIDHI/OneDrive/Documents/My Karier/money-alfian-main/index.html', 'utf8');
const checks = [
    'id="langSelect"',
    'changeLanguage',
    'uploadProfilePhoto',
    'loadProfilePhoto',
    'initLanguage',
    'showContactModal',
    'closeContactModal',
    'contactModal',
    'wa.me/6285732491409',
    'alfiangopoh09@gmail.com',
    'appTranslations',
    'generateLocalFallback',
    'avatarUpload',
    'nav-label-home'
];
checks.forEach(c => {
    console.log((html.includes(c) ? 'FOUND' : 'MISSING') + ': ' + c);
});
console.log('Total file size:', html.length);

