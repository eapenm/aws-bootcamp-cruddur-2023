-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Eapen Mani','eapenmani@yahoo.com' , 'eapenm' ,'MOCK'),
  ('Robin Mani','eapenmani@gmail.com' , 'robinm' ,'MOCK'),
  ('Londo Mollari', 'lmollari@centari.com','londo','MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'eapenm' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )