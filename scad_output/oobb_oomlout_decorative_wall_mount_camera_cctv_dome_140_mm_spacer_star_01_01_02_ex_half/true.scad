$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-32.0000000000, 32.0000000000, 0]) {
				cylinder(h = 2, r = 5);
			}
			translate(v = [32.0000000000, 32.0000000000, 0]) {
				cylinder(h = 2, r = 5);
			}
			translate(v = [-32.0000000000, -32.0000000000, 0]) {
				cylinder(h = 2, r = 5);
			}
			translate(v = [32.0000000000, -32.0000000000, 0]) {
				cylinder(h = 2, r = 5);
			}
		}
	}
	union() {
		translate(v = [30, 0, -100.0000000000]) {
			cylinder(h = 200, r = 1.5000000000);
		}
		translate(v = [-30, 0, -100.0000000000]) {
			cylinder(h = 200, r = 1.5000000000);
		}
		translate(v = [0, -30, -100.0000000000]) {
			cylinder(h = 200, r = 1.5000000000);
		}
		translate(v = [0, 30, -100.0000000000]) {
			cylinder(h = 200, r = 1.5000000000);
		}
		translate(v = [65, 65, 0.0000000000]) {
			cylinder(h = 2, r = 67.5000000000);
		}
		translate(v = [-65, 65, 0.0000000000]) {
			cylinder(h = 2, r = 67.5000000000);
		}
		translate(v = [65, -65, 0.0000000000]) {
			cylinder(h = 2, r = 67.5000000000);
		}
		translate(v = [-65, -65, 0.0000000000]) {
			cylinder(h = 2, r = 67.5000000000);
		}
		translate(v = [-250, 5, -250]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [-250, 5, -250]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [-250, 5, -250]) {
			cube(size = [500, 500, 500]);
		}
	}
}