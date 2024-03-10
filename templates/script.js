// JavaScript code for countdown animation
document.addEventListener('DOMContentLoaded', function() {
  const countdowns = document.querySelectorAll('.countdown');

  countdowns.forEach(countdown => {
    const target = +countdown.innerText; // Get the target count

    // Start the countdown animation
    let current = 1;
    const interval = setInterval(() => {
      if (current <= target) {
        countdown.innerText = current;
        current++;
      } else {
        clearInterval(interval);
      }
    }, 1000); // Update every second
  });
});
