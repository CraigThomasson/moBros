const categoryHeaders = document.querySelectorAll('.category-header');
const messageContainer = document.querySelector('.message-container');

categoryHeaders.forEach((categoryHeader) => {
    categoryHeader.addEventListener('click', () => {
        console.log("clicked")
    });
});

// change style to hide after 5 seconds

setTimeout(() => {messageContainer.style.visibility = 'hidden'}, 5000);