import sys
import re

from toy_robot_simulator import Simulator


def apply_cmd(sim, cmd):
    """
    For each robot cmd input line, apply the cmd to simulator
    """
    result = None
    cmd = cmd.strip().upper()

    match_place = re.match(r'PLACE\s*(\d+)\s*,\s*(\d+)\s*,\s*(\w+)', cmd)
    if match_place:
        # apply PLACE command
        x, y, direction = match_place.group(1, 2, 3)
        x, y = int(x), int(y)
        result = sim.place(x, y, direction)
    else:
        # try to apply all other commands
        valid_cmds = {
            'MOVE': 'move',
            'LEFT': 'left',
            'RIGHT': 'right',
            'REPORT': 'report',
        }
        if cmd in valid_cmds.keys():
            result = getattr(sim, valid_cmds[cmd])()
        else:
            # noop if cmd is invalid
            pass

    if cmd == 'REPORT':
        print("Output: {}".format(result))
    return result


def main(input_filename=None):
    if input_filename:
        with open(input_filename) as f:
            input_cmds = f.readlines()
    else:
        input_cmds = sys.stdin

    debug = False
    sim = Simulator()
    for input_cmd in input_cmds:
        result = apply_cmd(sim, input_cmd)
        if debug:
            print("input:{} result:{} robot:{}".format(input_cmd, result,
                                                       sim.robot))


if __name__ == '__main__':
    main()
