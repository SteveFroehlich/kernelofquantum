    (function(){
      $(".math").each(function() {
        var texTxt = $(this).text();
        el = $(this).get(0);
        console.log("data: " + el)
        if(el.tagName == "DIV"){
            addDisp = "\\displaystyle";
        } else {
            addDisp = "";
        }
        try {
            katex.render(addDisp+texTxt, el);
        }
        catch(err) {
            $(this).html("<span class='err'>"+err);
        }
      }); 
    })();

    function toggleAnswer() {
      $(".answer").toggle();
    }

    function toggleSolution() {
      $(".solution").toggle();
    }
