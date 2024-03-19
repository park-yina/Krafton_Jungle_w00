// 이미지를 클릭하면 모달을 열고 이미지를 모달에 표시하는 함수
function openModal() {
    // 모달 열기
    const modal = document.getElementById('modal');
    modal.classList.remove('hidden');
    
    // 클릭된 이미지의 src 가져오기
    const clickedImageSrc = this.getAttribute('src');
    
    // 모달에 이미지 표시
    const modalImage = document.getElementById('modal-image');
    modalImage.setAttribute('src', clickedImageSrc);
}

// 모달을 닫는 함수
function closeModal() {
    const modal = document.getElementById('modal');
    modal.classList.add('hidden');
}

// 닫기 버튼에 이벤트 리스너 추가
const closeModalButton = document.getElementById('close-modal');
closeModalButton.addEventListener('click', closeModal);

// 각 이미지에 모달 열기 이벤트 리스너 추가
const images = document.querySelectorAll('.open-modal');
images.forEach(image => {
    image.addEventListener('click', openModal);
});
