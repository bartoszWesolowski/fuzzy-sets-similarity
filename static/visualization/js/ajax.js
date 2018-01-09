function addslashes(str) {
     return (str + '')
        .replace(/[\\"']/g, '\\$&')
        .replace(/\u0000/g, '\\0');
}

var currentCaller;
var currentRoot2;
var currentNumber;

function refreshFilters(){

    changeFilterAjax(currentCaller,currentRoot2,currentNumber);
}

function getAll(caller,root2,number){

    $.each($("#data"+number+" input[name='category[]']"),function(i,v){
        $(this).attr("checked","checked");
    });

    changeFilterAjax(caller,root2,number);
}

function changeFilterAjax(caller,root2, number){

    currentCaller = caller;
    currentRoot2 = root2;
    currentNumber = number;

    var checked = []
    $("#data"+number+" input[name='category[]']:checked").each(function ()
    {
        checked.push(parseInt($(this).val()));
    });
    caller = $(caller);

    actionLink = caller.attr("action");
    //console.log(caller);
    $.ajax({
        type: "POST",
        url: actionLink,
        dataType:"json",
        data: { number: checked,root2:root2 },
        success: function (data) {
            if(!data.errors){

                var href="gdzie-jechac-poi/";
                if(number==1)
                    href="co-robic-poi/";
                if(number==2)
                    href="gdzie-spac-poi/";
                if(number==3)
                    href="co-gdzie-kiedy-poi/";

                href=baseDir+href;

                m.removeMarkers();

                var firstPoint = null;

                if(m.points.length>0)
                    firstPoint =m.points[0];

                m.removePoints();

                if(firstPoint!=null) {
                    m.addMarker(firstPoint.id, firstPoint.y, firstPoint.x, firstPoint.title, firstPoint.descr, firstPoint.icon);
                }

                $("#filter"+number+" ul").empty();
                $.each(data,function(index,value){

                    if(firstPoint!=null && (firstPoint.id==value.product_id)){

                    }else {
                        m.addMarker(value.product_id, value.coord_y, value.coord_x, addslashes(value.name), '<a href="' + href + value.product_id + '">' + addslashes(value.name) + '</a>', value.icon);
                    }
                    if(m.currentMarkerInScope)
                        $("#filter"+number+" ul").append('<li><a href="'+href+value.product_id+'">'+value.name+'</a></li>');
                });

                $("#filter"+number).pajinate({items_per_page: 9});

            }
            else displayProductUnavailableNotice(caller,data.errors);
        }
    });
}