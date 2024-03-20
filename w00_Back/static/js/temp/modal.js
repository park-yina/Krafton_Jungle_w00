 
        function openModal() {
            // 클릭된 이미지의 위치를 가져옵니다.
            const imageRect = this.getBoundingClientRect();
            const imageTop = imageRect.top;
            const imageLeft = imageRect.left;

            // 모달의 위치를 이미지 근처로 이동시킵니다.
            const modal = document.getElementById('modal');
            modal.style.top = `${imageTop}px`;
            modal.style.left = `${imageLeft}px`;
            
            // 클릭된 이미지의 ID를 가져옵니다.
            const imageId = this.getAttribute('data-id');
            
            // 해당 이미지의 스토리 및 이미지 URL을 가져옵니다.
            const story = dummy.find(item => item.id === parseInt(imageId)).story;
            const imageUrl = dummy.find(item => item.id === parseInt(imageId)).img;
            
            // 모달에 이미지 및 스토리를 표시합니다.
            const modalImage = document.getElementById('modal-image');
            modalImage.setAttribute('src', imageUrl);
            
            const modalStory = document.getElementById('modal-story');
            modalStory.textContent = story;
            
            // 모달을 엽니다.
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }

        function closeModal() {
            const modal = document.getElementById('modal');
            modal.classList.add('hidden');
            document.body.style.overflow = 'auto';
        }

        const closeModalButton = document.getElementById('close-modal');
        closeModalButton.addEventListener('click', closeModal);

        const images = document.querySelectorAll('.open-modal');
        images.forEach(image => {
            image.addEventListener('click', openModal);
        });