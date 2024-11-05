document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.action-button');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const userId = this.dataset.userId; // Получите ID пользователя из атрибута data
            if (userId) {
                toggleBlockUser(userId);
            } else {
                console.error('User ID is not defined');
            }
        });
    });
});

console.log(`/auth/block/${userId}`);  // Убедитесь, что это соответствует маршруту
const response = await fetch(`/auth/block/${userId}`, { method: 'POST' });

