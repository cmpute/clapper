# Clapper - Perception Extension for CLAP framework
This repo forks base on commit [`90f1fd3ac7b35eeea391fa4d2fa8cd11e7e73d18`](https://gitlab.com/umvdl/zzz/zzz/-/tree/90f1fd3ac7b35eeea391fa4d2fa8cd11e7e73d18) of original repo. The codebase should be able to be combined by cherry picking commits of this repo after `afb19bfc43d3a88bd49c3707cc1918f857ef6f2f`.

# Usage

## Carla with ros bridge
1. Run docker or local binary. Export port to 2000, 2001
1. Start roscore separately
1. Go to ros bridge repo, source `devel/setup.bash` and launch `src/driver/simulators/carla/carla_adapter/launch/server.launch`
1. Go to this repo, source `devel/setup.bash` and launch `src/driver/simulators/carla/carla_adapter/scripts/use_bridge/main.launch`

## Carla with scenario_runner
1. Run docker or local binary. Export port to 2000, 2001
1. Start roscore separately
1. Set `TEAM_CODE_ROOT` to `src/driver/simulators/carla/carla_adapter/scripts/use_srunner`
1. Run srunner command: `python ${ROOT_SCENARIO_RUNNER}/srunner/challenge/challenge_evaluator_routes.py --scenarios=${ROOT_SCENARIO_RUNNER}/srunner/challenge/all_towns_traffic_scenarios1_3_4.json --agent=${TEAM_CODE_ROOT}/ZZZAgent.py`

> See `zzz/src/driver/simulators/carla/carla_adapter/scripts/server.tmuxp.yaml` for details
