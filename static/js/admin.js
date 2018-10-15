(function() {
    var $ = django.jQuery;
    $(document).on('change', 'select[name=name]', function(e) {
        $('.set-logo').attr('src', `https://images.pokemontcg.io/${e.target.value}/logo.png`);
    });
})();