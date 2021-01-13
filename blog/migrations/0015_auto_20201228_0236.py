# Generated by Django 2.2.10 on 2020-12-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20201228_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multistepformmodel',
            name='prjfield',
            field=models.CharField(choices=[('Fintech', 'Fintech'), ('Cloud/Sass', 'Cloud/Sass'), ('Agritech (agriculture de précision)', 'Agritech (agriculture de précision)'), ('Economie circulaire (greentech)', 'Economie circulaire (greentech)'), ('E-learning/ Edtech', 'E-learning/ Edtech'), ('Govtech (e-administration)', 'Govtech (e-administration)'), ('IOT (internet des objets)', 'IOT (internet des objets)'), ('Legaltech', 'Legaltech'), ('Food tech', 'Food tech'), ('E-health (santé)', 'E-health (santé)'), ('Smart City', 'Smart City'), ('IOT (internet des objets)', 'IOT (internet des objets)'), ('Tourisme/voyage', 'Tourisme/voyage'), ('Energies renouvelables', 'Energies renouvelables'), ('Pharma', 'Pharma'), ('Education', 'Education'), ('Intelligence Artificielle', 'Intelligence Artificielle'), ('Réalité augmentée/virtuelle', 'Réalité augmentée/virtuelle'), ('E-services', 'E-services'), ('Economie sociale et solidaire.', 'Economie sociale et solidaire.'), ('Cybersecurity', 'Cybersecurity'), ('Electronique &amp; Composants', 'Electronique &amp; Composants'), ('Jeux/loisir', 'Jeux/loisir'), ('Autre', 'Autre')], max_length=225),
        ),
    ]