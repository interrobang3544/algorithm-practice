def draw(scale):
    if scale == 3:
        return ['***','* *','***']

    star_unit = draw(scale // 3)
    star_res = []

    for star in star_unit: star_res.append(star * 3)
    for star in star_unit: star_res.append(star + ' ' * (scale//3) + star)
    for star in star_unit: star_res.append(star * 3)

    return star_res

N = int(input())
print('\n'.join(draw(N)))