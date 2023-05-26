window.addEventListener('DOMContentLoaded', function() {
    var welcomeMessage = 'Welcome to my about page!';
    alert(welcomeMessage);
});

document.addEventListener('DOMContentLoaded', function() {
    // // Check if dark mode preference is set
    const prefersDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  
    // Retrieve dark mode preference from localStorage
    const storedDarkMode = localStorage.getItem('darkMode');
  
    // Set initial dark mode state based on preference
    const darkModeEnabled = storedDarkMode !== null ? JSON.parse(storedDarkMode) : prefersDarkMode;
  
    // Update dark mode toggle button text
    const toggleButton = document.getElementById('darkModeToggle');
    toggleButton.textContent = darkModeEnabled ? 'Disable Dark Mode' : 'Enable Dark Mode';
  
    // Apply dark mode styles
    function enableDarkMode() {
        document.body.classList.add('dark-mode');
        document.querySelector('header').style.backgroundColor = '#181818';
        document.querySelector('footer').style.backgroundColor = '#181818';
        document.querySelector('main sidebar').style.backgroundColor = '#181818';
        document.querySelector('h1').style.color = '#ffffff'; // Set h1 text color to white
        localStorage.setItem('darkMode', true);
        toggleButton.textContent = 'Disable Dark Mode';
    }
  
    // Remove dark mode styles
    function disableDarkMode() {
        document.body.classList.remove('dark-mode');
        document.querySelector('header').style.backgroundColor = '#eee';
        document.querySelector('footer').style.backgroundColor = '#eee';
        document.querySelector('main sidebar').style.backgroundColor = '#eee';
        document.querySelector('h1').style.color = '#333333'; // Set h1 text color to default
        localStorage.setItem('darkMode', false);
        toggleButton.textContent = 'Enable Dark Mode';
    }
  
    // Toggle dark mode when button is clicked
    toggleButton.addEventListener('click', function() {
        if (document.body.classList.contains('dark-mode')) {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });
  
    // Set initial dark mode state
    if (darkModeEnabled) {
        enableDarkMode();
    }
});