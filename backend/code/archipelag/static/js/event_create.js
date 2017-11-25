$(document).ready(function() {
    loadDatePickers();
    listenOnSaveMarket();

});

function listenOnSaveMarket(){
        const button = document.getElementById("create_event");
        button.addEventListener("click", createEvent);
}

function loadDatePickers(){
   $('#dpd1').datetimepicker({
       format: 'YYYY-MM-DD HH:mm',
       })
    $('#dpd2').datetimepicker({
        useCurrent: false,
        format: 'YYYY-MM-DD HH:mm',
    });
    $("#dpd1").on("dp.change", function (e) {
        $('#dpd2').data("DateTimePicker").minDate(e.date);
    });
    $("#dpd2").on("dp.change", function (e) {
        $('#dpd1').data("DateTimePicker").maxDate(e.date);
    });
}

function getInputValues(){
    const title = $("#title").val();
    const url = $("#url").val();
    const hashtag = $("#hashtag").val();
    const dateFrom = $("#dpd1").find("input").val();;
    const dateTo = $("#dpd2").find("input").val();
    return{
        title:title,
        url:url,
        hashtag:hashtag,
        dateFrom:dateFrom,
        dateTo:dateTo}
}

function isInputHasRequiredFields(requiredFields, testedDict){

    let missingField = ""
    $.each(requiredFields, function( index, value ) {
      if (testedDict[value] == ""){
          missingField = value;
      }
          return false;
    });
    if (missingField == ""){
        return true;
    }else{
        return false;
    }

}

function createEvent(data){
    inputValues = getInputValues()

    requiredFields = ['url', 'hashtag', 'title', 'dateFrom',"dateTo"]
    if (isInputHasRequiredFields(requiredFields, inputValues) == true){
        sendInputs();
    }else{
        alert("Proszę o wypełnieni wszystkich pól.")
    }

};

function sendInputs(){
        const token = getCookieData("csrftoken");
	  $.ajax({
	      type:"POST",
          url:"/market/create/",
          contentType: 'application/json; charset=utf-8',
          headers: {'X-CSRFToken': token},
          data:JSON.stringify(getInputValues()),
          dataType: 'json',
                success:function(data)
					{
                        console.log(data)
                	},
				error:function( xhr,textStatus,err)
					{
                        console.log(err)
					}
});
}

function getCookieData( name ) {
    var pairs = document.cookie.split("; "),
        count = pairs.length, parts;
    while ( count-- ) {
        parts = pairs[count].split("=");
        if ( parts[0] === name )
            return parts[1];
    }
    return false;
}