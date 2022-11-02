// // make the navbar sticky on scroll
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    var floatLimit = navbar.offsetTop + navbar.offsetHeight;
    navbar.classList.toggle('fixed-top', window.pageYOffset > 1);
    navbar.classList.toggle('menu__fixed', window.pageYOffset > 1);
});
