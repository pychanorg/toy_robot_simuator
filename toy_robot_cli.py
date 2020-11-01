import sys
import re

from toy_robot_simulator import Simulator


def apply_cmd(sim, cmd):
    """
    For each robot cmd input line, apply valid cmds and args to simulator
    """
    result = None
    cmd = cmd.strip().upper()

    matching_cmds = {
        # contains matching_regex and sim function name
        # this is conceptually similar to Django's URLconf
        r'PLACE\s*(\d+)\s*,\s*(\d+)\s*,\s*(\w+)': 'place',
        r'MOVE': 'move',
        r'LEFT': 'left',
        r'RIGHT': 'right',
        r'REPORT': 'report',
    }

    for matching_regex, matching_function in matching_cmds.items():
        match_result = re.match(matching_regex, cmd)
        if match_result:
            sim_args = match_result.groups()
            sim_function_name = getattr(sim, matching_function)
            result = sim_function_name(*sim_args)

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
