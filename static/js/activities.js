const categoryHeaders = document.querySelectorAll('.category-header');
const messageContainer = document.querySelectorAll('.message-container');

categoryHeaders.forEach((categoryHeader) => {
    categoryHeader.addEventListener('click', () => {
        console.log("clicked")
    });
});


setTimeout(() => messageContainer.classList.add = 'hide', 5000);