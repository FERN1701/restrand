document.addEventListener("DOMContentLoaded", function() {
    // Show the terms and conditions modal
    const termsModal = new bootstrap.Modal(document.getElementById('termsModal'));
    termsModal.show();

    // Ensure the modal is not blocking form submission
    document.getElementById('agreeButton').addEventListener('click', function() {
        termsModal.hide();
    });
});
