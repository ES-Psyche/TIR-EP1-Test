# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.
        


init python:


    def scale_proportionally(img):
        currentwidth, currentheight = get_size(img)
        xscale = float(config.screen_width) / float(currentwidth)
        yscale = float(config.screen_height) / float(currentheight)

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return im.FactorScale(img,minscale,minscale)

    def get_size(d):
        d = renpy.easy.displayable(d)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h   
    
    
    config.rollback_enabled = True

# Loads images

    ##def load_images(path_start, extensions=['.jpg', '.png'], filename_only=False):
        #for file in renpy.list_files():
            #if file.startswith(path_start):
                #for extension in extensions:
                    #if file.endswith(extension):
                        #if filename_only:
                            #name = file.replace(path_start, '').split('/')[-1].replace(extension,'')
                        #else:
                            #name = file.replace(path_start, '').replace('/', ' ').replace(extension,'')
                        #renpy.image(name, Image(file))

    ##load_images('common/images/')
    ##load_images('chapters/', filename_only=True)


label start:

    # jump prologue
    jump test_new_phone


label splashscreen:
    
$ renpy.movie_cutscene('es.ogv')
   
with fade

$ renpy.movie_cutscene('tir.ogv')
   
scene disclamer with Dissolve(3.0)
pause(1.0)



    

return

