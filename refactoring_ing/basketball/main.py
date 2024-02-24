from refactoring_ing.basketball.aug_16_basketball import Player, Guard, Forward, Center

if __name__ == '__main__':
    heo_hun = Player("허훈", 180)
    heo_hun.classification()

    heo_ung = Guard("허웅", 183, 30)
    heo_ung.assist()
    heo_ung.dribbling()
    heo_ung.three_points_shoot()

    choi_junyong = Forward("최준용", 198, 50)
    choi_junyong.rebound()
    choi_junyong.block_shoot()

    ra_guna = Center("라건아", 200, 500)
    ra_guna.dunk()