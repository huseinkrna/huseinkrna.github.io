document.addEventListener('DOMContentLoaded', function () {

    // 💡 FITUR 1: EFEK KETIKAN (TYPED.JS)
    if (document.getElementById('profile-name-typed')) {
        var options = {
            strings: ["Husein Kurnia Riyadinata", "Seorang Mahasiswa", "Seorang Desainer", "Seorang Public Speaker"], // Teks yang ingin diketik
            typeSpeed: 50, // Kecepatan mengetik
            backSpeed: 25, // Kecepatan menghapus
            loop: true,    // Mengulang terus-menerus
            showCursor: true,
            cursorChar: '_',
        };
        new Typed('#profile-name-typed', options);
    }

    // 🖼️ FITUR 2: MODAL UNTUK CV
    const cvModal = document.getElementById('cv-modal');
    const cvButton = document.getElementById('cv-button');
    const closeButton = document.querySelector('.close-button');

    if (cvModal && cvButton && closeButton) {
        // Saat tombol CV diklik, tampilkan modal
        cvButton.onclick = function (event) {
            event.preventDefault(); // Mencegah link default
            cvModal.style.display = 'block';
        }

        // Saat tombol 'x' diklik, sembunyikan modal
        closeButton.onclick = function () {
            cvModal.style.display = 'none';
        }

        // Jika user mengklik di luar area modal, sembunyikan juga
        window.onclick = function (event) {
            if (event.target == cvModal) {
                cvModal.style.display = 'none';
            }
        }
    }
    
    // 🚀 FITUR 3: AMBIL PROYEK DARI GITHUB
    async function getGithubProjects() {
        const username = 'huseinkrna'; // Ganti dengan username GitHub Anda
        const projectsContainer = document.getElementById('github-projects');

        if (!projectsContainer) return; // Hentikan jika elemen tidak ada

        try {
            // Ambil data 3 repo terakhir yang di-update
            const response = await fetch(`https://api.github.com/users/${username}/repos?sort=updated&per_page=3`);
            
            if (!response.ok) {
                throw new Error('Gagal mengambil data dari GitHub');
            }

            const projects = await response.json();
            
            // Kosongkan kontainer
            projectsContainer.innerHTML = '';

            // Tampilkan setiap proyek
            if(projects.length > 0) {
                projects.forEach(project => {
                    const projectCard = `
                        <div class="project-card">
                            <h3><a href="${project.html_url}" target="_blank">${project.name}</a></h3>
                            <p>${project.description || 'Tidak ada deskripsi.'}</p>
                        </div>
                    `;
                    projectsContainer.innerHTML += projectCard;
                });
            } else {
                 projectsContainer.innerHTML = `<p>Tidak ada repositori publik yang bisa ditampilkan.</p>`;
            }

        } catch (error) {
            projectsContainer.innerHTML = `<p>Gagal memuat proyek. Coba lagi nanti.</p>`;
            console.error(error);
        }
    }

    // Panggil fungsi ini saat halaman dimuat
    getGithubProjects();
});
