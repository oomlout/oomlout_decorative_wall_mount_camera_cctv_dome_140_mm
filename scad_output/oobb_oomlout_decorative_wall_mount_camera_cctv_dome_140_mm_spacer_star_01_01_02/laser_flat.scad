$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 0.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
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
						rotate(a = [0, 0, 45]) {
							hull() {
								translate(v = [-9.5000000000, 9.5000000000, 0]) {
									cylinder(h = 5, r = 5);
								}
								translate(v = [9.5000000000, 9.5000000000, 0]) {
									cylinder(h = 5, r = 5);
								}
								translate(v = [-9.5000000000, -9.5000000000, 0]) {
									cylinder(h = 5, r = 5);
								}
								translate(v = [9.5000000000, -9.5000000000, 0]) {
									cylinder(h = 5, r = 5);
								}
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
					}
				}
			}
		}
	}
}