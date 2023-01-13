from flet import *
class CustomCheckBox(UserControl):
  def __init__(self,color,label='',selection_fill='#183588',size=25,stroke_width=2,animation=None, checked=False, font_size=17, pressed=None):
    super().__init__()
    self.selection_fill = selection_fill
    self.color = color
    self.label = label
    self.size = size
    self.stroke_width = stroke_width
    self.animation=animation
    self.checked=checked
    self.font_size=font_size
    self.pressed  = pressed
  def _checked(self):
      self.check_box = Container(
        animate=self.animation,
        width=self.size,height=self.size,
        border_radius=(self.size/2)+5,
        bgcolor=self.CHECKED,
        content=Icon(icons.CHECK_ROUNDED,size=15,),)
      return self.check_box
  
  def _unchecked(self):
    self.check_box = Container(
      animate=self.animation,
      width=self.size,height=self.size,
      border_radius=(self.size/2)+5,
      bgcolor=None,
      border = border.all(color=self.color,width=self.stroke_width),
      content=Container(),
      ) 
    return self.check_box

  def build(self):
    self.BG = '#041955'
    self.FG = '#3450a1'
    self.PINK = '#eb06ff'
    self.CHECKED = '#183588'

    if self.checked == True:  
      return Column(controls=[
        Container(
          on_click = lambda e: self.checked_check(e),
          content=Row(
            controls=[
          self._checked(),
          Text(self.label,
                font_family='poppins',
                size=self.font_size,
                weight=FontWeight.W_300,),
        ]))
      ])
      
    else:  
      return Column(
        controls=[
        Container(on_click = lambda e: self.checked_check(e),
          content=Row(
            controls=[
          self._unchecked(),
          Text(self.label,
                font_family='poppins',
                size=self.font_size,
                weight=FontWeight.W_300,),
        ]))
      ])

  def checked_check(self,e):
    print(self.checked)
    if self.checked == False:
        self.checked = True
        self.check_box.border = None
        self.check_box.bgcolor = self.CHECKED
        self.check_box.content = Icon(icons.CHECK_ROUNDED,size=15,)
        self.update()

        
    elif self.checked == True:
        self.checked = False
        self.check_box.bgcolor = None
        self.check_box.border = border.all(color=self.color,width=self.stroke_width)
        self.check_box.content.visible = False
        self.update()
        

    if self.pressed:
      self.run()       
  def is_checked(self):
      return self.checked

  def run(self,*args):
    self.pressed(args)