ori_cells = float(input('Original cell suspension concentration in cells/ml:'))
# ori_volume = input('Total volume of original cell suspension in ml:')
desired_conc = float(input('Desired cells concentration in cells/well:'))
desired_vol = float(input('Desired volume per well in ul:'))
num_wells = 4 + float(input('Number of wells:'))
# dilution_factor = ori_cells /desired_conc
volume_from_stock = num_wells * (1000/(ori_cells/desired_conc))
seeding_vol = num_wells * desired_vol
pure_medium = seeding_vol - volume_from_stock 

print(f'Volume from cell stock in ul: {volume_from_stock:2f}')
print(f'Volume of pure medium in ul: {pure_medium}') 

