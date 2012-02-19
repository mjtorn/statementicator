# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.db.transaction import commit_on_success

from django.core.management.base import BaseCommand, CommandError

from statementicatordb import parser

from optparse import make_option

class Command(BaseCommand):
    """Command the parsing of a file
    """

    help = 'Read a statemnt file'

    args = 'statement_file'

    option_list = BaseCommand.option_list + (
        make_option('--bic', action='store', dest='bic', help='Your BIC'),
        make_option('--format', action='store', dest='format', help='File format'),
    )

    @commit_on_success
    def handle(self, *args, **options):
        """Executioner
        """

        if not options['bic'] or not options['format'] or not args:
            self.stdout.write('%s\n' % self.print_help('read_file', 'read_file'))
            return

        parser_class = getattr(parser, options['format'], None)
        if parser_class is None:
            supported = ', '.join([c for c in dir(parser) if not c.startswith('_')])
            raise CommandError('Unknown format. Supported: %s' % supported)

        lines = open(args[0], 'rb').readlines()

        parser_instance = parser_class.Parser(options['bic'], lines)

        parser_instance.run()

# EOF

