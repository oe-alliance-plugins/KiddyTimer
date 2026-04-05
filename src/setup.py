from setuptools import setup
import setup_translate

pkg = 'Extensions.KiddyTimer'
setup(name='enigma2-plugin-extensions-kiddytimer',
       version='3.0',
       description="Allows to control the Kids' daily TV usage",
       package_dir={pkg: 'KiddyTimer'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'img/*.png', 'KiddyTimer.png', 'LICENSE', 'maintainer.info', 'keymap.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
