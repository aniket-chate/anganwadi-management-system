// ======================================================
// Anganwadi Management System
// script.js
// ======================================================


// =========================================
// Auto Close Flash Messages
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.classList.remove("show");

            alert.classList.add("fade");

            setTimeout(function () {

                alert.remove();

            }, 500);

        }, 4000);

    });

});


// =========================================
// Delete Confirmation
// =========================================

function confirmDelete(name = "this beneficiary") {

    return confirm(

        `Are you sure you want to delete ${name}?`

    );

}


// =========================================
// Prevent Double Form Submission
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const submitButton = form.querySelector(

                "button[type='submit']"

            );

            if (submitButton) {

                submitButton.disabled = true;

                submitButton.innerHTML =
                    '<span class="spinner-border spinner-border-sm"></span> Processing...';

            }

        });

    });

});


// =========================================
// Bootstrap Tooltips
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    const tooltipTriggerList = [].slice.call(

        document.querySelectorAll('[data-bs-toggle="tooltip"]')

    );

    tooltipTriggerList.map(function (tooltipTriggerEl) {

        return new bootstrap.Tooltip(

            tooltipTriggerEl

        );

    });

});


// =========================================
// Search Input Auto Focus
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.querySelector(

        "input[name='name']"

    );

    if (searchInput) {

        searchInput.focus();

    }

});


// =========================================
// Highlight Selected Row
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    const rows = document.querySelectorAll("tbody tr");

    rows.forEach(function (row) {

        row.addEventListener("click", function () {

            rows.forEach(function (r) {

                r.classList.remove("table-active");

            });

            row.classList.add("table-active");

        });

    });

});


// =========================================
// Smooth Scroll
// =========================================

document.querySelectorAll("a[href^='#']").forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(

            this.getAttribute("href")

        );

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});


// =========================================
// Loading Spinner
// =========================================

window.addEventListener("load", function () {

    const loader = document.querySelector(".loader");

    if (loader) {

        loader.style.display = "none";

    }

});


// =========================================
// Form Validation
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function (e) {

            const requiredFields = form.querySelectorAll(

                "[required]"

            );

            let valid = true;

            requiredFields.forEach(function (field) {

                if (field.value.trim() === "") {

                    valid = false;

                    field.classList.add("is-invalid");

                } else {

                    field.classList.remove("is-invalid");

                }

            });

            if (!valid) {

                e.preventDefault();

                alert(

                    "Please fill all required fields."

                );

            }

        });

    });

});


// =========================================
// Dashboard Counter Animation
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    const counters = document.querySelectorAll("h3");

    counters.forEach(function (counter) {

        const value = Number(counter.innerText);

        if (!isNaN(value)) {

            let count = 0;

            const speed = Math.max(10, value / 40);

            const update = () => {

                count += speed;

                if (count < value) {

                    counter.innerText = Math.floor(count);

                    requestAnimationFrame(update);

                } else {

                    counter.innerText = value;

                }

            };

            update();

        }

    });

});


// =========================================
// Console Welcome
// =========================================

console.log(

    "Anganwadi Management System Loaded Successfully"

);