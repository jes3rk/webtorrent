import libtorrent as lt
import time

def handle(req):
    """
    req: {
        magnet: str => magnet link
    }
    """
    ses = lt.session()

    handle = lt.add_magnet_uri(ses, req['magnet'], {
        'save_path': '/tmp/torrent'
    })

    while (not handle.has_metadata()): time.sleep(1)

    s = h.status()
    print('starting', s.name)

    while (not s.is_seeding):
        s = h.status()

        print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
            s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
            s.num_peers, s.state), end=' ')

        alerts = ses.pop_alerts()
        for a in alerts:
            if a.category() & lt.alert.category_t.error_notification:
                print(a)

        sys.stdout.flush()

        time.sleep(1)

    print(h.status().name, 'complete')
    
    return req
