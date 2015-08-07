(function($){
    $(document).ready(function() {
        $('body').ud_initialize();
    });
    $('.ud-signup-popup-hook').on("load", function(){
        $(this).ud_initialize();
    });
})(jQuery);
