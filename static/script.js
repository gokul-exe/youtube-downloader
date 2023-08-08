document.getElementById("downloadForm").addEventListener("submit", function (event) {
  event.preventDefault();

  // Get the download button and the progress bar
  const downloadButton = document.getElementById("downloadButton");
  const progressBar = document.querySelector(".progress-bar");

  // Disable the button to prevent multiple clicks
  downloadButton.disabled = true;

  // Add progress-active class to trigger the animation
  progressBar.parentElement.classList.add("progress-active");

  // After the download is complete, submit the form
  setTimeout(() => {
      downloadButton.disabled = false;
      progressBar.parentElement.classList.remove("progress-active");
      event.target.submit();
  }, 2000); // Simulate a 5-second download process (adjust as needed)
});
