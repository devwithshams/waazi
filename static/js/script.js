document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase();
      const cards = document.querySelectorAll('.card');
      cards.forEach(card => {
        const name = card.querySelector('.card-title').textContent.toLowerCase();
        card.parentElement.parentElement.style.display = name.includes(query) ? 'block' : 'none';
      });
    });
  }
});

