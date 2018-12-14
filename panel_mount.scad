// specified parameters
panel_width = 162;
window_width = 156;
frame_thickness = 2;
edge_width = 2;

// calculated parameters
frame_width = panel_width + 2*edge_width;

difference() {
    cube([frame_width, frame_width, 2*frame_thickness], center=true);
    cube([window_width, window_width, 2.01*frame_thickness], center=true);
    translate([0, 0, frame_thickness])
        cube([panel_width, panel_width, 2*frame_thickness], center=true);
}
