from django.http import HttpResponse



site = '''
<!DOCTYPE html>
<html>
<body>

<div class='teste' onclick="myFunction()"
style="
    border: 1px solid red;
    width:100px;
    height:100px;
"></div>


<script>
function myFunction() {
        var squ = document.querySelector('.teste')
        var mouse_axis_x = event.clientX
        var mouse_axis_y = event.clientY
        squ.style.background = 'red';
        
}
</script>
</body>
</html>

'''


def index(request):
    return HttpResponse(site) 



