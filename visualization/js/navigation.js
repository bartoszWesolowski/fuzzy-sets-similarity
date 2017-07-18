(($) =>{
const rootTemplate = `
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Fuzzy Set Similarity</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="minkowski.html">Minkowski</a></li>
      <li><a href="angulardistance.html">Angular Dinstance</a></li>
    </ul>
  </div>
</nav>`

$('#navigation').append(rootTemplate);

})($);