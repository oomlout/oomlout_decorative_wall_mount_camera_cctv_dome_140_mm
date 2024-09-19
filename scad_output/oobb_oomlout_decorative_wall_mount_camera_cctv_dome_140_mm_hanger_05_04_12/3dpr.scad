$fn = 50;


difference() {
	union() {
		translate(v = [0, -7.5000000000, 0]) {
			hull() {
				translate(v = [-32.0000000000, 24.5000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [32.0000000000, 24.5000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [-32.0000000000, -24.5000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [32.0000000000, -24.5000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [30, 15, 12]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
						translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r1 = 2.1250000000, r2 = 4.3750000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.1250000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 15, 12]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
						translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r1 = 2.1250000000, r2 = 4.3750000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.1250000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-30, 15, 12]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
						translate(v = [0, 0, -3.7000000000]) {
							cylinder(h = 3.7000000000, r1 = 2.1250000000, r2 = 4.3750000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.1250000000);
						}
						translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 2.0000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-250.0000000000, -494, -491]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [-250.0000000000, -494, -491]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [-250.0000000000, -494, -491]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [30, 0, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [-30, 0, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [0, -30, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [0, 30, -100.0000000000]) {
			cylinder(h = 200, r = 1.8000000000);
		}
		translate(v = [65, -65, 0.0000000000]) {
			cylinder(h = 12, r = 67.5000000000);
		}
		translate(v = [-65, -65, 0.0000000000]) {
			cylinder(h = 12, r = 67.5000000000);
		}
	}
}