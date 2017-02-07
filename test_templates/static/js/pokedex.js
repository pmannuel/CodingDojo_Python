for (var i = 1; i <= 151; i++) {
    var new_pokemon_icon = "<div class='listbox'><img class='pokemon' id='" + i + "' src='http://pokeapi.co/media/img/" + i + ".png' alt=''></div>"
    console.log(new_pokemon_icon);
    $("#poke_icon").append(new_pokemon_icon);
}

$("img.pokemon").click(function() {
            console.log("clicked the poke icon");

            var index = this.id;
            // console.log(index);

            var pokemon_api = "http://pokeapi.co/api/v1/pokemon/" + index + "/";

            $.get(pokemon_api, function(data) {
                console.log("I am retrieving the pokemon api index: " + index);
                console.log(data);

                //    Adding Name of Pokemon     //
                var name_str = data.name;
                console.log(name_str);
                $("#name_info").html(name_str);

                //    Changing picture of Pokemon     //
                var img_str = "http://pokeapi.co/media/img/" + index + ".png";
                $("#img_info").attr("src", img_str);

                //    Adding Type of Pokemon     //
                var type_str = "";
                type_str += "<h3>Types</h3>";
                type_str += "<ul>";
                for (var i = 0; i < data.types.length; i++) {
                    type_str += "<li>" + data.types[i].name + "</li>";
                }
                type_str += "</ul>";
                $("#type_info").html(type_str);

                //    Adding Height of Pokemon     //
                var height_str = "";
                height_str = "<h3>Height</h3><ul>" + data.height[0] + "</li></ul>";
                $("#height_info").html(height_str);

                //    Adding Weight of Pokemon     //
                var weight_str = "";
                weight_str = "<h3>Weight</h3><ul>" + data.weight[0] + "</li></ul>";
                $("#weight_info").html(weight_str);

            }, "json");
        }
