/*
    Function to use Katex to render LaTex based math
*/
    (function(){
      $(".math").each(function() {
        var texTxt = $(this).text();
        el = $(this).get(0);
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

/*
    Functions to expand and collapse answers and solutions
*/
    function toggleAnswer() {
      $(".answer").toggle();
    }
    function toggleSolution() {
      $(".solution").toggle();
    }
