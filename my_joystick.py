
from donkeycar.parts.controller import Joystick, JoystickController


class MyJoystick(Joystick):
    #An interface to a physical joystick available at /dev/input/js0
    def __init__(self, *args, **kwargs):
        super(MyJoystick, self).__init__(*args, **kwargs)

            
        self.button_names = {
            0x134 : 'y',
            0x130 : 'b',
            0x131 : 'a',
            0x133 : 'x',
            0x137 : 'r',
            0x139 : 'zr',
            0x136 : 'l',
            0x138 : 'zl',
            0x13c : 'home',
            0x13b : 'plus',
            0x13a : 'minus',
            0x135 : 'circle',
        }


        self.axis_names = {
            0x0 : 'steering',
            0x4 : 'throttle',
        }



class MyJoystickController(JoystickController):
    #A Controller object that maps inputs to actions
    def __init__(self, *args, **kwargs):
        super(MyJoystickController, self).__init__(*args, **kwargs)


    def init_js(self):
        #attempt to init joystick
        try:
            self.js = MyJoystick(self.dev_fn)
            self.js.init()
        except FileNotFoundError:
            print(self.dev_fn, "not found.")
            self.js = None
        return self.js is not None


    def init_trigger_maps(self):
        #init set of mapping from buttons to function calls
            
        self.button_down_trigger_map = {
            'x' : self.toggle_mode,
            'y' : self.erase_last_N_records,
            'zl' : self.emergency_stop,
            'zr' : self.increase_max_throttle,
            'r' : self.decrease_max_throttle,
            'a' : self.toggle_constant_throttle,
            'b' : self.toggle_manual_recording,
        }


        self.axis_trigger_map = {
            'steering' : self.set_steering,
            'throttle' : self.set_throttle,
        }


