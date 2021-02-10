import json
import requests

data =[{'timehour':"03-03-2020 2:00", 'subsystem':"Welder 1", 'amplitude_mean':66.8, 'amplitude_max_2_mean':71.15, 'apparent_power_mean':623.1, 'apparent_power_max_mean':683.5, 'cycle_time_mean':1.96, 'depth_rpn_mean':0.21, 'depth_rpn_after_hold_time_mean':0.28, 'distance_abs_mean':63.01, 'energy_mean':41.45, 'frequency_mean':19842.05, 'joining_velocity_mean_mean':2.43, 'mains_supply_mean':228.12, 'mean_power_mean':360.65, 'power_end_mean':600, 'power_max_2_mean':621.15, 'pre_trigger_position_mean':60.76, 'temperature_mean':29.04, 'trigger_position_mean':62.8, 'trigger_position_max_mean':63.78, 'trigger_position_min_mean':61.74, 'unique_error_mean':0, 'weld_time_mean':0.11, 'amplitude_sd':2.98, 'amplitude_max_2_sd':1.63, 'apparent_power_sd':46.43, 'apparent_power_max_sd':31.46, 'cycle_time_sd':0.03, 'depth_rpn_sd':0, 'depth_rpn_after_hold_time_sd':0.01, 'distance_abs_sd':0.01, 'energy_sd':4.83, 'frequency_sd':2.14, 'joining_velocity_sd_sd':0.16, 'mains_supply_sd':0.38, 'sd_power_sd':17.41, 'power_end_sd':47.74, 'power_max_2_sd':36.38, 'pre_trigger_position_sd':0, 'temperature_sd':0.03, 'trigger_position_sd':0.01, 'trigger_position_max_sd':0, 'trigger_position_min_sd':0, 'unique_error_sd':0, 'weld_time_sd':0.01, 'bad_part':1, 'total_part':196,'reject_percent':0.51}]


url = 'http://0.0.0.0:5010/predict_api'


r = requests.post(url, json=data)
print(r.text)
