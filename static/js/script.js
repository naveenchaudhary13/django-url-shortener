// Toggle mobile menu
document.addEventListener("DOMContentLoaded", () => {
	const toggle = document.getElementById("navToggleBtn");
	const menu = document.getElementById("navMobileMenu");
	toggle.addEventListener("click", () => {
		menu.classList.toggle("hidden");
	});
});

// Show toast messages
function showToast(message, type = "success") {
	const container = document.getElementById("toast-container");
	if (!container) return;

	const toast = document.createElement("div");
	toast.className = `toast toast-${type} relative`;

	toast.innerHTML = `
    <span class="mr-2">${message}</span>
    <button onclick="this.parentElement.remove()" class="text-white font-bold ml-2"><i class="fa-solid fa-xmark"></i></button>
    <div class="toast-bar bg-white"></div>
  `;

	container.appendChild(toast);

	let start = Date.now();
	let remaining = 4000;
	let timer = setTimeout(() => toast.remove(), remaining);

	toast.addEventListener("mouseenter", () => {
		clearTimeout(timer);
		remaining -= Date.now() - start;
		toast.querySelector(".toast-bar").style.animationPlayState = "paused";
	});

	toast.addEventListener("mouseleave", () => {
		start = Date.now();
		timer = setTimeout(() => toast.remove(), remaining);
		toast.querySelector(".toast-bar").style.animationPlayState = "running";
	});
}

// Copy short URL
function copyToClipboard() {
	const urlText = document.getElementById("shortUrlText").textContent;
	navigator.clipboard.writeText(urlText).then(() => {
		showToast("Link copied!", "success");
	});
}

// Shorten URL and display result with AJAX
document.getElementById("shortenForm").addEventListener("submit", function (e) {
	e.preventDefault();

	fetch("", {
		method: "POST",
		body: new FormData(this),
		headers: { "X-Requested-With": "XMLHttpRequest" },
	})
		.then((res) => res.json())
		.then((data) => {
			showToast(data.message, data.type);
			if (data.success) {
				document.getElementById("resultBox").innerHTML = data.html;
			}
		});
});

// Show/Hide modals
function openModal(id) {
	document.getElementById(id).classList.remove("hidden");
}
function closeModal(id) {
	document.getElementById(id).classList.add("hidden");
}

// Toggle password
function togglePassword(inputId, iconSpan) {
	const input = document.getElementById(inputId);
	const icon = iconSpan.querySelector("i");
	if (input.type === "password") {
		input.type = "text";
		icon.classList.remove("fa-eye");
		icon.classList.add("fa-eye-slash");
	} else {
		input.type = "password";
		icon.classList.remove("fa-eye-slash");
		icon.classList.add("fa-eye");
	}
}
