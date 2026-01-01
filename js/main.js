document.getElementById('navToggle')?.addEventListener('click', function(){
  var nav = document.getElementById('nav');
  if(!nav) return;
  nav.style.display = nav.style.display === 'block' ? 'none' : 'block';
});

// Optional: intercept contact form and show simple success message (still posts to Formspree)
var form = document.getElementById('contactForm');
if(form){
  form.addEventListener('submit', function(e){
    // allow normal submit — Formspree will handle
    setTimeout(function(){
      alert('Thanks — your message is sent.');
    }, 600);
  });
}
