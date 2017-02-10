$('input.find_gold').click(function(){
    log = "Earned " + {{session['earned']}} + " from the " + {{session['location']}}
    $('#activities').html(log)
})
