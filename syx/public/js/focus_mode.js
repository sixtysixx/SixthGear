$(document).ready(function() {
    // Add Focus Mode button to navbar
    let add_focus_button = function() {
        if ($('#focus-mode-btn').length > 0) return;

        let btn = $(`<li class="nav-item">
            <a class="nav-link" id="focus-mode-btn" title="Focus Mode">
                <i class="fa fa-eye-slash"></i>
            </a>
        </li>`);

        $('.navbar-right .nav:first').prepend(btn);

        btn.on('click', function() {
            toggle_focus_mode();
        });
    };

    let toggle_focus_mode = function() {
        $('body').toggleClass('focus-mode');

        if ($('body').hasClass('focus-mode')) {
            // Apply styles
            $('<style id="focus-mode-style">' +
              '.layout-side-section { display: none !important; }' +
              '.layout-main-section { margin-left: auto !important; margin-right: auto !important; max-width: 900px !important; }' +
              '.navbar { display: none !important; }' +
              '#focus-mode-exit { position: fixed; top: 10px; right: 10px; z-index: 9999; }' +
              '</style>').appendTo('head');

            // Add exit button
            $('<button class="btn btn-secondary btn-xs" id="focus-mode-exit"><i class="fa fa-times"></i> Exit Focus</button>')
                .appendTo('body')
                .click(function() {
                    toggle_focus_mode();
                });

            frappe.show_alert("Focus Mode Enabled");
        } else {
            $('#focus-mode-style').remove();
            $('#focus-mode-exit').remove();
            frappe.show_alert("Focus Mode Disabled");
        }
    };

    // Frappe sometimes re-renders navbar, so we might need to retry or hook into events.
    // A simple timeout or interval check for MVP.
    setTimeout(add_focus_button, 2000);
});
