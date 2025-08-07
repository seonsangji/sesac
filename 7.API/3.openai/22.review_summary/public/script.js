console.log("JS 연결 성공")

const submitBtn = document.getElementById('submit-button');

submitBtn.addEventListener('click', submitReview);

async function submitReview() {
    const rating = document.querySelector('input[name="rating"]:checked')
    const opinion = document.getElementById('opinion').value;

    if (!rating || !opinion.trim()) {
        alert('평점 또는 후기가 입력되지 않았습니다.')
        return;
    }

    const review = {
        'rating': parseInt(rating.value),
        'opinion': opinion
    }

    const response = await fetch('/api/review', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(review)
    });
    
    fetchReviews();
    fetchAISummary();
}

async function fetchReviews() {
    const response = await fetch('/api/review');
    if (!response.ok) {
        throw new Error('요청 오류')
    }
    const data = await response.json();
    reviews = data.reviews;
    console.log(reviews);

    displayReview(reviews);
}

function displayReview(reviews) {
    const reviewContainer = document.getElementById('reviews-container');
    reviewContainer.querySelectorAll('.review-box').forEach(box => box.remove())
    reviews.forEach(review => {
        const reviewRow = document.createElement('div');
        reviewRow.className = 'review-box';
        reviewRow.innerHTML = `
            <p class="review-header">Rating: ${review.rating}</p>
            <p>${review.opinion}</p>   
        `
        reviewContainer.appendChild(reviewRow);
    })
}

async function fetchAISummary() {
    const lang = document.getElementById('languageSelect').value;

    const response = await fetch(`/api/ai-summary?lang=${lang}`);
    const data = await response.json();

    displayAISummary(data);
}

function displayAISummary(data) {
    const summaryBox = document.querySelector('.ai-summary');
    summaryBox.innerHTML = `
        <p><strong>AI 요약:</strong> ${data.summary}</p>
        <p><strong>평균 별점:</strong> ${data.averageRating.toFixed(2)}</p>
    `
}

window.onload = async () => {
    await fetchReviews()
    await fetchAISummary();
}