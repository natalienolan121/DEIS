import pandas
import json
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins
import plotly.graph_objects as go
from plotly.offline import plot

df = pandas.read_csv('Deis Review.csv')
from PIL import Image, ImageDraw, ImageFont
print(df)

def create_text_image(data_column, output_file_name, title):
    # Combine all text into a single string
    all_text = "\n".join([entry.strip() for entry in data_column.dropna() if entry.strip()])

    # Define image properties
    image_width = 2500
    image_height = 1500
    background_color = "white"
    text_color = "black"

    # Create an image canvas
    image = Image.new("RGB", (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(image)

    # Define font (default font as fallback)
    try:
        font = ImageFont.truetype("arial.ttf", 20)  # Adjust the font size as needed
    except:
        font = ImageFont.load_default()

    # Add title and text to the image
    margin = 20
    line_spacing = 10
    current_height = margin

    # Add title at the top
    draw.text((margin, current_height), title, fill="blue", font=font)
    current_height += font.getsize(title)[1] + line_spacing * 2  # Move below title

    # Add barriers text
    for line in all_text.split("\n"):
        draw.text((margin, current_height), line, fill=text_color, font=font)
        current_height += font.getsize(line)[1] + line_spacing  # Move to the next line

    # Save the image with a unique name
    image.save(output_file_name)
    print(f"Text image saved as: {output_file_name}")


#NUMERACY
effective_numeracy=df['How effective do you think our current numeracy initiatives have been in improving student outcomes?'].tolist()
numeracy_effectiveness1=effective_numeracy.count('Somewhat ineffective')
numeracy_effectiveness2=effective_numeracy.count('Somewhat effective')
numeracy_effectiveness3=effective_numeracy.count('Very ineffective')
numeracy_effectiveness4=effective_numeracy.count('Very effective')
numeracy_effectiveness5=effective_numeracy.count('Neither effective nor ineffective')
#print(effective_numeracy)
print("Somewhat Ineffective:",numeracy_effectiveness1)
print("Somewhat Effective:",numeracy_effectiveness2)
print("Very Ineffective:",numeracy_effectiveness3)
print("Very Effective:",numeracy_effectiveness4)
print("Neither:",numeracy_effectiveness5)

group_numeracy=["Very Effective","Somewhat Effective","Neither","Somewhat Ineffective","Very Ineffective"]
result_numeracy=[numeracy_effectiveness4, numeracy_effectiveness2, numeracy_effectiveness5,numeracy_effectiveness1,numeracy_effectiveness3]

fig = go.Figure(data=[go.Bar(
    x=group_numeracy,
    y=result_numeracy,
    text=[f"Value: {v}" for v in result_numeracy],  # Tooltip text
    hoverinfo='text',  # Enables text on hover
    marker=dict(color='lightblue', line=dict(color='black', width=1))
)])

# Customize the Chart
fig.update_layout(
    title='Interactive Bar Chart with Hover Tooltips',
    xaxis_title='Effecctiveness',
    yaxis_title='Values',
)

# Save the chart as an HTML file
output_file = 'numeracy_chart.html'
plot(fig, filename=output_file, auto_open=False)

numeracy_column = "What are the main barriers preventing students from improving their numeracy skills?"
create_text_image(df[numeracy_column], "numeracy_barriers_text.png", "Numeracy Barriers")

numeracyideas_column = "What initiatives or actions could help reduce numeracy anxiety among students?"
create_text_image(df[numeracyideas_column], "numeracy_ideas_text.png", "Numeracy Ideas")

numeracyideas2_column = "Do you have any additional feedback or suggestions for improving numeracy in our school?"
create_text_image(df[numeracyideas2_column], "numeracy_ideas2_text.png", "Numeracy Ideas2")




effective_literacy=df['How effective do you think our current literacy initiatives have been in improving student outcomes?'].tolist()
literacy_effectiveness1=effective_literacy.count('Somewhat ineffective')
literacy_effectiveness2=effective_literacy.count('Somewhat effective')
literacy_effectiveness3=effective_literacy.count('Very ineffective')
literacy_effectiveness4=effective_literacy.count('Very effective')
literacy_effectiveness5=effective_literacy.count('Neither effective nor ineffective')
#print(effective_numeracy)
print("Somewhat Ineffective:",literacy_effectiveness1)
print("Somewhat Effective:",literacy_effectiveness2)
print("Very Ineffective:",literacy_effectiveness3)
print("Very Effective:",literacy_effectiveness4)
print("Neither:",literacy_effectiveness5)

#LITERACY

group_literacy=["Very Effective","Somewhat Effective","Neither","Somewhat Ineffective","Very Ineffective"]
result_literacy=[literacy_effectiveness4, literacy_effectiveness2, literacy_effectiveness5,literacy_effectiveness1,literacy_effectiveness3]

fig = go.Figure(data=[go.Bar(
    x=group_literacy,
    y=result_literacy,
    text=[f"Value: {v}" for v in result_literacy],  # Tooltip text
    hoverinfo='text',  # Enables text on hover
    marker=dict(color='pink', line=dict(color='black', width=1))
)])

# Customize the Chart
fig.update_layout(
    title='Interactive Bar Chart with Hover Tooltips',
    xaxis_title='Effectiveness',
    yaxis_title='Values',
)

# Save the chart as an HTML file
output_file = 'literacy_chart.html'
plot(fig, filename=output_file, auto_open=False)

literacy_column = "What are the main barriers preventing students from improving their literacy skills?"
create_text_image(df[literacy_column], "literacy_barriers_text.png", "Literacy Barriers")

literacyideas_column = "What initiatives could help further improve literacy among students with EAL needs?"
create_text_image(df[literacyideas_column], "literacy_ideas_text.png", "Literacy Ideas")

literacyideas2_column = "What initiatives could help further improve literacy among students with EAL needs?"
create_text_image(df[literacyideas2_column], "literacy_ideas2_text.png", "Literacy Ideas")






effective_attendance=df['How effective do you think our current attendance initiatives have been in reducing absenteeism?'].tolist()
attendance_effectiveness1=effective_attendance.count('Somewhat ineffective')
attendance_effectiveness2=effective_attendance.count('Somewhat effective')
attendance_effectiveness3=effective_attendance.count('Very ineffective')
attendance_effectiveness4=effective_attendance.count('Very effective')
attendance_effectiveness5=effective_attendance.count('Neither effective nor ineffective')
#print(effective_numeracy)
print("Somewhat Ineffective:",attendance_effectiveness1)
print("Somewhat Effective:",attendance_effectiveness2)
print("Very Ineffective:",attendance_effectiveness3)
print("Very Effective:",attendance_effectiveness4)
print("Neither:",attendance_effectiveness5)



#ATTENDANCE
group_attendance=["Very Effective","Somewhat Effective","Neither","Somewhat Ineffective","Very Ineffective"]
result_attendance=[attendance_effectiveness4, attendance_effectiveness2, attendance_effectiveness5,attendance_effectiveness1,attendance_effectiveness3]
#plt.bar(group_attendance,result_attendance)
#plt.show()
fig = go.Figure(data=[go.Bar(
    x=group_attendance,
    y=result_attendance,
    text=[f"Value: {v}" for v in result_attendance],  # Tooltip text
    hoverinfo='text',  # Enables text on hover
    marker=dict(color='lightblue', line=dict(color='black', width=1))
)])

# Customize the Chart
fig.update_layout(
    title='Interactive Bar Chart with Hover Tooltips',
    xaxis_title='Effecctiveness',
    yaxis_title='Values',
)

# Save the chart as an HTML file
output_file = 'interactive_plotly_chart.html'
plot(fig, filename=output_file, auto_open=False)

attendance_column = "What barriers do you feel are preventing students from improving their attendance?"
create_text_image(df[attendance_column], "attendance_barriers_text.png", "Attendance Barriers")

attendance_ideas="How can we better support teachers in monitoring and improving student attendance?"
create_text_image(df[attendance_ideas], "attendance_ideas_text.png", "Attendance Ideas")

attendance_ideas2="Is there any Ideas that you have in or out of the classroom that could help improve attendance "
create_text_image(df[attendance_ideas2], "attendance_ideas2_text.png", "Attendance Ideas")




