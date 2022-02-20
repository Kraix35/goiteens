import areas_data as ad

def compare_areas(first_area, second_area):
    if first_area[1] > second_area[1]:
        print(f'{first_area[0]} area > {second_area[0]} area')
    elif first_area[1] < second_area[1]:
        print(f'{first_area[0]} area < {second_area[0]} area')
    elif first_area[1] == second_area[1]:
        print(f'areas are aqual')

compare_areas(ad.circle_area(10), ad.rectangle_area(2,7))