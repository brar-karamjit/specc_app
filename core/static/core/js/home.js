document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('[data-nav-toggle]');
    const menu = document.querySelector('[data-nav-menu]');

    if (!toggle || !menu) {
        return;
    }

    const closeMenu = () => {
        toggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('nav__links--open');
    };

    const openMenu = () => {
        toggle.setAttribute('aria-expanded', 'true');
        menu.classList.add('nav__links--open');
    };

    toggle.addEventListener('click', () => {
        const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
        if (isExpanded) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    menu.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => {
            if (window.matchMedia('(max-width: 768px)').matches) {
                closeMenu();
            }
        });
    });
});
