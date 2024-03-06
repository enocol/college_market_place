document.addEventListener("DOMContentLoaded", function() {
    let viewDetailsLinks = document.querySelectorAll(".view-details");
    
    viewDetailsLinks.forEach(function(link) {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            
            let card = this.closest(".card");
            let description = card.querySelector(".description");
            let cover = card.querySelector(".cover");
            
            // Toggle description visibility
            description.style.display = description.style.display === "none" ? "block" : "none";
            
            // Toggle flip class to trigger flip-back transition
            card.classList.toggle("flipped");
            
            // Remove flip class after the transition
            setTimeout(() => {
                card.classList.remove("flipped");
            }, 2300);
        });
    });
});
