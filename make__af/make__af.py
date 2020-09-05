import numpy as np


# ========================================================= #
# ===  make__af.py ( for superfish )                    === #
# ========================================================= #

def make__af():

    # ------------------------------------------------- #
    # --- [1] Load parameters                       --- #
    # ------------------------------------------------- #
    
    a = 11
    b = 41.13
    d = 34.955
    t = 5.0
    r = 2.5
    f = 2.856
    delta = 1.0
    
    outFile = "basicCavity.af"
    
    print()
    print( "[make__af]  outFile :: {0}".format( outFile ) )
    print()

    # ------------------------------------------------- #
    # --- [2] comment & settings part               --- #
    # ------------------------------------------------- #
    
    comment  = \
        "### {0} GHz Cavity\n"\
        "### squared shape cavity with a bore tube\n"\
        "### created by K.Nishida (2020/08)\n"\
        "\n\n".format( f )
    
    settings = \
        "&reg kprob=1,    ! superfish problem\n"\
        "icylin=1,        ! cylindrical geometry\n"\
        "freq={0},        ! RF Frequency\n"\
        "dx={1},          ! mesh interval\n"\
        "xdri=0,ydri=5,   ! Drive point of RF\n"\
        "kmethod=1,       ! Use beta to compute wave number\n"\
        "beta=0.95 &      ! Particle velocity for transit-time integrals\n"\
        "\n\n".format( f, delta )


    # ------------------------------------------------- #
    # --- [3] coordinate settings                   --- #
    # ------------------------------------------------- #

    pts      = [ [                 0.0,    0.0 ],
                 [                 0.0,      b ],
                 [         0.5*d-0.5*t,      b ],
                 [         0.5*d-0.5*t,    a+r ],
                 [         0.5*d+0.5*t,    a+r ],
                 [         0.5*d+0.5*t,      b ],
                 [     d + 0.5*d-0.5*t,      b ],
                 [     d + 0.5*d-0.5*t,    a+r ],
                 [     d + 0.5*d+0.5*t,    a+r ],
                 [     d + 0.5*d+0.5*t,      b ],
                 [ 2.0*d + 0.5*d-0.5*t,      b ],
                 [ 2.0*d + 0.5*d-0.5*t,    a+r ],
                 [ 2.0*d + 0.5*d+0.5*t,    a+r ],
                 [ 2.0*d + 0.5*d+0.5*t,      b ],
                 [ 3.0*d              ,      b ],
                 [ 3.0*d              ,    0.0 ],
                 [                 0.0,    0.0 ]
    ]
    pts      = np.array( pts )
    
    x_,y_    = 0, 1
    geometry = ""
    npts     = pts.shape[0]
    for ik in range( npts ):
        geometry += "$po x={0}, y={1} $\n".format( pts[ik,x_], pts[ik,y_] )

    # ------------------------------------------------- #
    # --- [4] write in a file                       --- #
    # ------------------------------------------------- #
        
    with open( outFile, "w" ) as f:
        f.write( comment  )
        f.write( settings )
        f.write( geometry )
        
    return()


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    make__af()
